## Топология:
![alt text](./screens/topology.PNG)

## Интерфейсы:
Маршрутизатор, эмулирующий интернет:
![alt text](./screens/inet_interfaces.PNG)

Пограничный маршрутизатор-1 (на нем настроены и GRE, и GRE + IPSec):
![alt text](./screens/vyos1_interfaces.PNG)

Пограничный маршрутизатор-2 (GRE):
![alt text](./screens/vyos2_interfaces.PNG)

Пограничный маршрутизатор-3 (GRE + IPSec):
![alt text](./screens/vyos3_interfaces.PNG)

## Пинги:
Пинги, исходящие от клиента-1 (vpc-1 на схеме):
![alt text](./screens/vyos1_pings.PNG)

Пинги приходящие к клиенту-1 от клиента-2 и клиента-3:
![alt text](./screens/vyos1_pongs.PNG)

Видно, что пакеты между клиентом-1 и клиентом-3 шифруются (использовалась аутентификация с обменом ключей).
