#TESTE CUCUMBER
Feature: Calculadora
    Como usuario
    Quero realizar somas na Calculadora
    Para verificar se os calculos estão corretos

  Scenario Outline: Soma dos numeros
    Given insiro o numero um "<num1>"
    And insiro o numero dois "<num2>"
    When clico no botão soma
    Then O resultado deve ser "<resultado>"

    Examples:
      | num1 | num2 | resultado |
      |    5 |    3 |         8 |
      |   10 |    7 |        17 |
      |    2 |   20 |        22 |