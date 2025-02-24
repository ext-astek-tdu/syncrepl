Feature: TODO: Find title

  Scenario Outline: I want my syncrepl client to bind to an openLDAP server with ldapurl
    Given Client is not bind to LDAP server
    When Client connect to "ldap://localhost:389/cn=admin,dc=openldapprov,dc=com??sub?(objectClass=*),X-BINDPW=admin" on "REFRESH_AND_PERSIST" mode
    Then Client has been binded to LDAP server

  Scenario Outline: I want my syncrepl client to bind to an openLDAP server with LDAPInfo object
    Given Client is not bind to LDAP server
    When Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
    Then Client has been binded to LDAP server
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_AND_PERSIST |
  
  Scenario Outline: I want my syncrepl client to detect an addition
    Given Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
    When I do a "ldapadd" on the openLDAP serveur, with this ldif file "addition.ldif"
    Then Client changed his infos according to ldif file "addition.ldif"
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_AND_PERSIST |
  
  Scenario Outline: I want my syncrepl client to detect a deletion
    Given  Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
    When I do a "ldapdelete" on the openLDAP serveur, with this ldif file "deletion.ldif"
    Then Client changed his infos according to ldif file "deletion.ldif"
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_AND_PERSIST |
  
  Scenario Outline: I want my syncrepl client to detect a renaming
    Given  Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
    When I do a "ldapmodify" on the openLDAP serveur, with this ldif file "renaming.ldif"
    Then Client changed his infos according to ldif file "renaming.ldif"
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_AND_PERSIST |
  
  Scenario Outline: I want my syncrepl client to detect a modification
    Given  Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
    When I do a "ldapmodify" on the openLDAP serveur, with this ldif file "modification.ldif"
    Then Client changed his infos according to ldif file "modification.ldif"
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_AND_PERSIST |
    
  # Scenario Outline: I want my syncrepl client to detect a cookie update
  #   Given  Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
  #   When I do a "ldapmodify" on the openLDAP serveur, with this ldif file "cookie_update.ldif"
  #   Then Client changed his infos according to ldif file "cookie_update.ldif"
  #   Examples:
  #     | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
  #     | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_AND_PERSIST |
