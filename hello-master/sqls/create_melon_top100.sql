drop table if exists SongArtist;
drop table if exists SongRank;
drop table if exists Song;
drop table if exists Album;
drop table if exists Artist;


create table Song(
    songno varchar(10) not null primary key,
    title varchar(255),
    genre varchar(31),
    albumid varchar(10),
    likecnt int
);

create table SongRank(
    id int auto_increment not null primary key,
    rankdt varchar(10),
    rank tinyint unsigned not null default 0,
    songno varchar(10)
);

create table Album(
    albumid varchar(10) not null primary key,
    title varchar(255),
    createdt varchar(10),
    company varchar(128),
    genre varchar(128),
    likecnt int,
    rate decimal(3,2),
    crawldt varchar(10)
);

create table Artist(
    artistid varchar(10) not null,
    name varchar(31) not null,
    atype tinyint(1) not null default 0,
    primary key(artistid, atype)
);

create table SongArtist(
    songno varchar(10),
    artistid varchar(10),
    atype tinyint(1) not null default 0,
    primary key(songno, artistid, atype)
);

alter table SongRank add constraint foreign key(songno) references Song(songno);
alter table Song add constraint foreign key(albumid) references Album(albumid);
alter table SongArtist add constraint foreign key(songno) references Song(songno);
alter table SongArtist add constraint foreign key(artistid) references Artist(artistid);