/*==============================================================*/
/* DBMS name:      Microsoft SQL Server 2008                    */
/* Created on:     26/04/2017 15:58:38                          */
/*==============================================================*/
CREATE DATABASE ZAPATERIA1

USE ZAPATERIA1


if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('PRODUCTO') and o.name = 'FK_PRODUCTO_RELATIONS_SUCURSAL')
alter table PRODUCTO
   drop constraint FK_PRODUCTO_RELATIONS_SUCURSAL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('VENTA') and o.name = 'FK_VENTA_RELATIONS_SUCURSAL')
alter table VENTA
   drop constraint FK_VENTA_RELATIONS_SUCURSAL
go

if exists (select 1
   from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
   where r.fkeyid = object_id('VENTA') and o.name = 'FK_VENTA_RELATIONS_PRODUCTO')
alter table VENTA
   drop constraint FK_VENTA_RELATIONS_PRODUCTO
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('PRODUCTO')
            and   name  = 'RELATIONSHIP_2_FK'
            and   indid > 0
            and   indid < 255)
   drop index PRODUCTO.RELATIONSHIP_2_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('PRODUCTO')
            and   type = 'U')
   drop table PRODUCTO
go

if exists (select 1
            from  sysobjects
           where  id = object_id('SUCURSAL')
            and   type = 'U')
   drop table SUCURSAL
go

if exists (select 1
            from  sysindexes
           where  id    = object_id('VENTA')
            and   name  = 'RELATIONSHIP_1_FK'
            and   indid > 0
            and   indid < 255)
   drop index VENTA.RELATIONSHIP_1_FK
go

if exists (select 1
            from  sysobjects
           where  id = object_id('VENTA')
            and   type = 'U')
   drop table VENTA
go

/*==============================================================*/
/* Table: PRODUCTO                                              */
/*==============================================================*/
create table PRODUCTO (
   ID_PROD              int                  not null,
   RUC_SUC              int                  null,
   NOM_PROD             varchar(20)          not null,
   MARCA_PROD           varchar(20)          not null,
   TALLA_PROD           int                  not null,
   COLOR_PROD           varchar(20)          not null,
   VU_PROD              decimal              not null,
   STOCK_PROD           int                  not null,
   constraint PK_PRODUCTO primary key nonclustered (ID_PROD)
)
go

/*==============================================================*/
/* Index: RELATIONSHIP_2_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_2_FK on PRODUCTO (
RUC_SUC ASC
)
go

/*==============================================================*/
/* Table: SUCURSAL                                              */
/*==============================================================*/
create table SUCURSAL (
   RUC_SUC              int                  not null,
   NOM_SUC              varchar(30)          not null,
   CIUDAD_SUC           varchar(15)          not null,
   DIR_SUC              varchar(30)          not null,
   TLF_SUC              int                  not null,
   constraint PK_SUCURSAL primary key nonclustered (RUC_SUC)
)
go

/*==============================================================*/
/* Table: VENTA                                                 */
/*==============================================================*/
create table VENTA (
   ID_VEN               int                  not null,
   RUC_SUC              int                  null,
   ID_PROD              int                  null,
   CANT_VEN             int                  not null,
   VT_VEN               decimal              not null,
   FECHA_VEN            date             null,
   constraint PK_VENTA primary key nonclustered (ID_VEN)
)
go

/*==============================================================*/
/* Index: RELATIONSHIP_1_FK                                     */
/*==============================================================*/
create index RELATIONSHIP_1_FK on VENTA (
RUC_SUC ASC
)
go

alter table PRODUCTO
   add constraint FK_PRODUCTO_RELATIONS_SUCURSAL foreign key (RUC_SUC)
      references SUCURSAL (RUC_SUC)
go

alter table VENTA
   add constraint FK_VENTA_RELATIONS_SUCURSAL foreign key (RUC_SUC)
      references SUCURSAL (RUC_SUC)
go

alter table VENTA
   add constraint FK_VENTA_RELATIONS_PRODUCTO foreign key (ID_PROD)
      references PRODUCTO (ID_PROD)
go


--VISTAS

USE ZAPATERIA1

SELECT * FROM PRODUCTO

SELECT * FROM VENTA

SELECT * FROM SUCURSAL


ALTER VIEW VENTAS
AS
	SELECT V.FECHA_VEN, P.NOM_PROD, SUM(V.CANT_VEN) AS CANTIDAD, SUM(V.VT_VEN)AS VENTA_TOTAL
		FROM VENTA V, PRODUCTO P
		WHERE V.ID_PROD=P.ID_PROD AND V.FECHA_VEN LIKE '2016-%-%'
		GROUP BY V.FECHA_VEN, P.NOM_PROD 

ALTER VIEW VENTAS1
AS
	SELECT V.FECHA_VEN, P.NOM_PROD, SUM(V.CANT_VEN) AS CANTIDAD, SUM(V.VT_VEN)AS VENTA_TOTAL
		FROM VENTA V, PRODUCTO P
		WHERE V.ID_PROD=P.ID_PROD AND V.FECHA_VEN LIKE '2015-%-%'
		GROUP BY V.FECHA_VEN, P.NOM_PROD

CREATE VIEW VENTAS2
AS
	SELECT V.FECHA_VEN, P.NOM_PROD, SUM(V.CANT_VEN) AS CANTIDAD, SUM(V.VT_VEN)AS VENTA_TOTAL, 
		FROM VENTA V, PRODUCTO P
		WHERE V.ID_PROD=P.ID_PROD AND V.FECHA_VEN LIKE '2014-%-%'
		GROUP BY V.FECHA_VEN, P.NOM_PROD 

SELECT * FROM VENTAS
SELECT * FROM VENTAS1
SELECT * FROM VENTAS2
