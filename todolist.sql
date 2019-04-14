create database todolist_db
use todolist_db

create table todo(
    todo_idx int auto_increment primary key,
    todo_content varchar(500) not null,
    todo_status int not null,
    todo_importance int not null
);