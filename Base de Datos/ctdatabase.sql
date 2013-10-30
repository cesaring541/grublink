/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     01/10/2013 11:26:38 AM                       */
/*==============================================================*/


drop table if exists ADMINISTRADOR;

drop table if exists GRUPO_INVESTIGACION;

drop table if exists INTEGRANTE;

drop table if exists PROYECTOS;

drop table if exists SEMILLERO;

/*==============================================================*/
/* Table: ADMINISTRADOR                                         */
/*==============================================================*/
create table ADMINISTRADOR
(
   ID_ADMINISTRADOR     numeric(8,0) not null,
   ID_GRUPO             numeric(8,0) not null,
   NOMBRE               varchar(100) not null,
   primary key (ID_ADMINISTRADOR)
);

/*==============================================================*/
/* Table: GRUPO_INVESTIGACION                                   */
/*==============================================================*/
create table GRUPO_INVESTIGACION
(
   ID_GRUPO             numeric(8,0) not null,
   NOMBRE_GRUPO         varchar(25) not null,
   REGISTRO_COLCIENCIAS varchar(20) not null,
   RANKING              numeric(20,0),
   FECHA_FUNDADO        date not null,
   primary key (ID_GRUPO)
);

/*==============================================================*/
/* Table: INTEGRANTE                                            */
/*==============================================================*/
create table INTEGRANTE
(
   ID_INTEGRANTE        numeric(8,0) not null,
   ID_SEMILLERO         numeric(1,0) not null,
   ID_GRUPO             numeric(8,0) not null,
   NOMBREINTEGRANTE     varchar(20) not null,
   DESCRIPCION          varchar(200) not null,
   FECHA_INGRESO        date not null,
   FECHA_SALIDA         date not null,
   CVLAC                varchar(20),
   TIPO_INTEGRANTE      varchar(20),
   primary key (ID_INTEGRANTE)
);

/*==============================================================*/
/* Table: PROYECTOS                                             */
/*==============================================================*/
create table PROYECTOS
(
   ID_PROYECTO          numeric(8,0) not null,
   PRO_ID_PROYECTO      numeric(8,0),
   ID_INTEGRANTE        numeric(8,0) not null,
   NOMBRE_PROYECTO      varchar(30),
   primary key (ID_PROYECTO)
);

/*==============================================================*/
/* Table: SEMILLERO                                             */
/*==============================================================*/
create table SEMILLERO
(
   ID_SEMILLERO         numeric(1,0) not null,
   ID_GRUPO             numeric(8,0) not null,
   DESCRIPCION_SEMILLERO varchar(200) not null,
   NOMBRE_SEMILLERO     varchar(25) not null,
   primary key (ID_SEMILLERO)
);

alter table ADMINISTRADOR add constraint FK_RELATIONSHIP_6 foreign key (ID_GRUPO)
      references GRUPO_INVESTIGACION (ID_GRUPO) on delete restrict on update restrict;

alter table INTEGRANTE add constraint FK_RELATIONSHIP_4 foreign key (ID_SEMILLERO)
      references SEMILLERO (ID_SEMILLERO) on delete restrict on update restrict;

alter table INTEGRANTE add constraint FK_RELATIONSHIP_5 foreign key (ID_GRUPO)
      references GRUPO_INVESTIGACION (ID_GRUPO) on delete restrict on update restrict;

alter table PROYECTOS add constraint FK_RELATIONSHIP_10 foreign key (ID_INTEGRANTE)
      references INTEGRANTE (ID_INTEGRANTE) on delete restrict on update restrict;

alter table PROYECTOS add constraint FK_RELATIONSHIP_9 foreign key (PRO_ID_PROYECTO)
      references PROYECTOS (ID_PROYECTO) on delete restrict on update restrict;

alter table SEMILLERO add constraint FK_RELATIONSHIP_7 foreign key (ID_GRUPO)
      references GRUPO_INVESTIGACION (ID_GRUPO) on delete restrict on update restrict;

