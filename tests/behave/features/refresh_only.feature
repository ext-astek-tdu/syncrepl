Feature: TODO: Find title

  Scenario Outline: I want my syncrepl client to bind to an openLDAP server with ldapurl
    Given Client is not bind to LDAP server
    When Client connect to "ldap://localhost:389/cn=admin,dc=openldapprov,dc=com??sub?(objectClass=*),X-BINDPW=admin" on "REFRESH_ONLY" mode
    Then Client has been binded to LDAP server

  Scenario Outline: I want my syncrepl client to bind to an openLDAP server with LDAPInfo object
    Given Client is not bind to LDAP server
    When Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
    Then Client has been binded to LDAP server
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_ONLY |
  
  Scenario Outline: I want my syncrepl client to detect an addition
    Given Client connect to dn:"<dn>" as bind_dn:"<bind_dn>" password:"<psswd>" filter:"<filter>" scope: "<scope>" mode:"<mode>"
    When TODO
    Then TODO
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_ONLY |
  
  Scenario Outline: I want my syncrepl client to detect a deletion
    Given TODO
    When TODO
    Then TODO
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_ONLY |
  
  Scenario Outline: I want my syncrepl client to detect a renaming
    Given TODO
    When TODO
    Then TODO
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_ONLY |
  
  Scenario Outline: I want my syncrepl client to detect a modification
    Given TODO
    When TODO
    Then TODO
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_ONLY |
    
  Scenario Outline: I want my syncrepl client to detect a cooki update
    Given TODO
    When TODO
    Then TODO
    Examples:
      | dn                     | bind_dn                         | psswd | filter          | scope         | mode         |
      | dc=openldapprov,dc=com | cn=admin,dc=openldapprov,dc=com | admin | (objectClass=*) | SCOPE_SUBTREE | REFRESH_ONLY |
