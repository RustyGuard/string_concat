Feature: Вывод в терминал
  Scenario: Вывод в терминал
    Given Не указан файла вывода
      When Утилита запущена
      Then Результирующая строка выведена в терминал