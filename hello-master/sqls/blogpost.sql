drop table if exists BlogPost;
drop table if exists Blogger;

create table Blogger(
    blogid varchar(64) not null primary key,
    name varchar(128),
    bloglink varchar(255)
);

create table BlogPost(
    id int not null auto_increment primary key,
    title varchar(255) not null,
    blogid varchar(64) not null,
    postdate varchar(8),
    posturl varchar(255)
);

alter table BlogPost add constraint foreign key(blogid) references Blogger(blogid);

