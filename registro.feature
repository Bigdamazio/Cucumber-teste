Feature: Registro de usuarios
    Como um novo usuario
    Quero registrar-me no sistema
    Para poder acessar as funcionalidades personalizadas

Background:
    Given estou no navegador chrome

Scenario: Registro de um usuario existente
    Given estou na pagina de registro
    When eu preencho o formulario de registro com dados existentes
    And clico no botao de registro
    Then devo ver uma mensagem de erro informando que o usuario ja existe

Scenario Outline: Registro de um usuario existente com diferentes dados
    Given estou na pagina de registro
    When eu preencho o formulario de registro com dados existentes com "<Nome>" e "<Sobrenome>"
    And clico no botao de registro
    Then devo ver uma mensagem de erro informando que o usuario ja existe

    Examples:
      | Nome  | Sobrenome |
      | Daniel | Damazio  |
      | Joao   | Silva    |
      | Maria  | Gomes    |

Scenario Outline: Registro de um usuario existente via diferentes plataformas
    Given estou na pagina de registro via "<Plataforma>"
    When eu preencho o formulario de registro com dados existentes
    And clico no botao de registro
    Then devo ver uma mensagem de erro informando que o usuario ja existe

    Examples:
      | Plataforma |
      | Google     |
      | Facebook   |
