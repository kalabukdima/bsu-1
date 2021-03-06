# Edit User Use Case

Вариант использования «Редактировать данные Пользователя»

## Short description

Краткое описание.

> Данный вариант описывает изменение `Администратором` (_Admin_) данных
> `Пользователей` (_Users_).

## Main actions flow

Основной поток событий

1. `Администратор` запрашивает список `Пользователей`.
2. `Система` отображает список `Пользователей`.
3. `Администратор` запрашивает данные `Пользователя` для редактирования.
4. `Система` отображает форму редактирования данных выбранного `Пользователя`.
5. `Администратор` заполняет форму и запрашивает сохранение данных.
6. `Система` сохраняет изменения в `Базу данных`.

## Alternative actions flows

Альтернативные потоки событий

#### `База данных` недоступна

> Если обнаруживается, что `База данных` c `Пользователями` недоступна,
> `Система` выдает сообщение об ошибке.

> После подтверждения сообщения `Администратором` вариант использования
> завершается.

#### `Администратор` отказывается от редактирования данных `Пользователя`

> Если `Администратор` отказывается от редактирования данных `Пользователя`, то
> вариант использования завершается.

## Pre-conditions

Предусловия

> `Администратор` авторизован в `Системе`.

## Post-conditions

Постусловия

> Данные `Пользователя` изменены.

---

[< Login](https://github.com/Drapegnik/bsu/blob/master/technology/lab2/docs/login.md)
| Edit User |
[Create Order >](https://github.com/Drapegnik/bsu/blob/master/technology/lab2/docs/create-order.md)
