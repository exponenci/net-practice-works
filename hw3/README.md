## Схема:
![alt text](./screens/topology.PNG)

## Клиенты

### Получение сетевых настроек по DHCP:
Первый клиент:
![alt text](./screens/client1_dhcp.PNG)

Второй клиент:
![alt text](./screens/client2_dhcp.PNG)
### Пинги:
Первый клиент (второго клиента и внешнего роутера):
![alt text](./screens/client1_pings.PNG)

Второй клиент (первого клиента и внешнего роутера):
![alt text](./screens/client2_pings.PNG)

## Конфигурации:
Конфигурация коммутаторов с первого дз не менялась. Основные изменения затронули первый (нижний) роутер.

Конфигурация dhcp:

![alt text](./screens/router_dhcp.PNG)

dhcp-leases после того, как какие-то клиенты получили настройки:
![alt text](./screens/router_dhcp_leases.PNG)

Трансляции SNAT после ping-ов (был реализован PAT по примеру из семинара, который менял source-адрес у запросов, подпадающих в указанное подмножество):
![alt text](./screens/router_snat_translations.PNG)
