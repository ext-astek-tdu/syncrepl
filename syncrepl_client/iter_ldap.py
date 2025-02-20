from collections.abc import Iterator, Mapping
import sqlite3


class ItemList(Mapping):
    """
    Let's make a class to represent our LDAP items!
    We implement the methods needed for a Dictionary.
    The keys are DNs; the values are attribute dicts.
    """

    # The only thing we need is a database cursor.
    def __init__(self, cursor):
        # Let the superclass set itself up.
        Mapping.__init__(self)

        # Store our cursor
        self.__syncrepl_cursor = cursor

        # Define attributes for our list of DNs, and the number of DNs.
        # These are lazily-populated by checking __syncrepl_count.
        self.__syncrepl_count = None
        self.__syncrepl_list = None

        # We also make a place to cache entries we've pulled.
        self.__syncrepl_attrlist = {}

    def __del__(self):
        try:
            self.__syncrepl_cursor.close()
        except sqlite3.ProgrammingError:
            pass

    def __syncrepl_populate(self):
        rowlist = []
        self.__syncrepl_cursor.execute(
            """
            SELECT dn
                FROM syncrepl_records
        """
        )
        for row in self.__syncrepl_cursor.fetchall():
            rowlist.append(row[0])
        self.__syncrepl_list = rowlist
        self.__syncrepl_count = len(rowlist)

    def __getitem__(self, dn):
        # Populate, and check cache.
        if self.__syncrepl_count is None:
            self.__syncrepl_populate()
        elif dn in self.__syncrepl_attrlist:
            return self.__syncrepl_attrlist[dn]

        # Check for the DN in the DB.
        # Cache the result for later use.
        self.__syncrepl_cursor.execute(
            """
            SELECT attributes
                FROM syncrepl_records
                WHERE dn = ?
        """,
            (dn,),
        )
        row = self.__syncrepl_cursor.fetchone()
        if row is not None:
            self.__syncrepl_attrlist[dn] = row[0]
            return row[0]

        raise KeyError(dn)

    def __iter__(self):
        # Populate the DNs first.
        if self.__syncrepl_count is None:
            self.__syncrepl_populate()

        class ItemIter(Iterator):
            """
            Make a small iterator class.
            NOTE: The only reason we just need a local index, is because
            this object is read-only.
            """

            def __init__(self, item_list):
                self.i = 0
                self.item_list = item_list

            def __next__(self):
                # Remember, i is zero-indexed
                if self.i >= len(self.item_list):
                    raise StopIteration
                dn = self.item_list[self.i]
                self.i += 1
                return dn

        # Give the iterator to the client, along with a list ref.
        return ItemIter(self.__syncrepl_list)

    def __len__(self):
        # Populate, and then return length.
        if self.__syncrepl_count is None:
            self.__syncrepl_populate()
        return self.__syncrepl_count
