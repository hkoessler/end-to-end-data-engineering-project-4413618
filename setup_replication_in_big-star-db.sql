alter table customers replica identity default;
alter table order_items replica identity default;
alter table orders replica identity default;
alter table products replica identity default;
select pg_create_logical_replication_slot('airbyte_slot', 'pgoutput');
create publication airbyte_publication for table customers, order_items, orders, products;
