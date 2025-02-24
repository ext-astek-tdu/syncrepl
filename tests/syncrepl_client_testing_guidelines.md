# Syncrepl Client Testing Guidelines

## Features to be Tested

The syncrepl client must work correctly in two modes:

- **`SyncreplMode.REFRESH_ONLY`**: The client polls the provider manually.
- **`SyncreplMode.REFRESH_AND_PERSIST`**: The client maintains a persistent connection and receives real-time updates.

## Things that Need to be Tested

The client must correctly handle the following operations via a callback class:

- **Binding to an LDAP server** using an `ldapurl` or an `LDAPInfo` object.
- **Detecting LDAP changes**:
  - Record addition
  - Record deletion
  - Record renaming
  - Record modification
  - Syncrepl cookie updates
- **Ensuring synchronization**:
  - When a refresh is completed, the client must be up to date.
  - These tasks must function correctly in both `REFRESH_ONLY` and `REFRESH_AND_PERSIST` modes.

Additionally, the client should allow the specification of filters and search scopes to determine which portions of the LDAP tree to replicate.

## Test Data: LDIF Files

To effectively test the client, we need a set of LDIF files representing different test scenarios:

We need a basic LDIF file that tests could run on it.

## Method to keep track of ldap changes

We should have a custom callback class that register every changes from the openLDAP server.