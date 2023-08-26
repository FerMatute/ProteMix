# ProteMix

## Description
Intelligent kiosk system that consists of a screen, which will display the interface where customers can access an intuitive and complete menu that will allow them to customize their drink according to their individual preferences. Likewise, they will be able to select the ingredients, the quantity of each ingredient, the size of the glass, among other available options. In addition, the system will provide detailed information on ingredients and possible combinations, in order to assist customers in their decision making. The ultimate goal is to bring convenience and efficiency to the ordering process, so that customers can get their drinks quickly and efficiently.

## Problem
Over the years the importance of maintaining a healthy and active lifestyle has become a culture for the community, but in situations where people are away from home or in a hurry to get to their destination, it does not allow them to eat the right way. For example, you may be heading to the gym, work or school and not have enough time to prepare a breakfast, or at least a protein shake, which may be difficult to acquire due to its limited availability in a few places. That is why, students of Robotics and Digital Systems Engineering at Tecnológico de Monterrey Campus Querétaro decided that a solution is required that allows people to place their orders for personalized drinks easily and accurately, thus optimizing their experience and satisfaction to complement a healthy diet.

## Materiales
- 1 Raspberrypi 

- 2 Bombas de agua

- 3 Servomotores

- 1 Sensor de ultrasónico

- 1 Display 5’’ Raspberry

- 1 Protoboard

- Arduino	2 Resistencias de 1kΩ

- 1 Manguera de ¼’’

- Tablones de MDF

- 4 Bisagras

- Cable

- Mouse alámbrico

## Functionality
The interface will be shown on the 5'' Display, where the user will select the desired protein, then the system will start its operation through the Raspberrypi which is responsible for receiving the information provided and will start the water pump to run the liquid up the hose, and receive the signal from the ultrasonic sensor to start filling the cup, then the sensor will detect when the cup is full and sends the signal to turn off the pump; after that, the servomotors will be activated to open the gates of the selected powder container and drop the powder into the tumbler. Finally, the user will be notified that his drink is ready.

