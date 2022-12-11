## Топология:
![alt text](./screens/topology.PNG)

## Пинги:
На первом клиенте (до роутера и второго клиента):
![alt text](./screens/vpc1.PNG)

На втором клиенте (до роутера и первого клиента):
![alt text](./screens/vpc2.PNG)

## Интерфейсы:
На маршрутизаторе:
![alt text](./screens/router_interfaces.PNG)

На корневом коммутаторе:
![alt text](./screens/switch_root_interfaces.PNG)

На коммутаторе, уходящем в подсеть vlan10:
![alt text](./screens/switch_1_interfaces.PNG)

На коммутаторе, уходящем в подсеть vlan20:
![alt text](./screens/switch_2_interfaces.PNG)

## STP
На корне (видно, что он выбран корневым коммутатором (был выбран по priority)):
![alt text](./screens/switch_root_sptree.PNG)
На коммутаторе-1:
![alt text](./screens/switch_1_sptree.PNG)
На коммутаторе-2:
![alt text](./screens/switch_2_sptree.PNG)
