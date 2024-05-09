# NL.ros2Obstacacle_avoidanceRobot

WAARSCHUWING! & Samenvatting:

dit is een ros2 obstacle avoidance robot in ROS2 Iron_irwini Framework. 
het is niet perfect.
het is bedoeld om zelf te calibreren voor je eigen doeleinde. deze project is gebruikt met 3d print files  van: https://openroboticplatform.com/(but je kan ook bouwen met je eigen onderdelen als wilt).
links zijn in de github repository of in de  video description (als er ruimte is voor in de text space).

AANGERADEN SKILLS NODIG:
python3,ROS2,robotica,coderen en kennis in ssh in vscode(alternatieven is optioneel),
3d printing,solderen.

3D Printe onderdelen (meestal PLA or PETG.links zijn in de github repository of in de  video description):

2x CheapyellowTTmotorholderV2.stl
1x d22powerbankholdeWidthV1-powerbankholder.stl
1x d22Rpiholderforhatsupport-Body.stl
1x JanSpiesZA-55-ORP_L298_Holder-Body_10mm_standoff.stl
1x nikodembartnik-4-plate_160mm_motors.3mf
1x nikodembartnik-4-plate_160mm.3mf
4x nikodembartnik-7-connector_60mm.3mf
2x nikodembartnik-11-tt_motor_wheel.3mf
1x Tenda-59-9V.3mf
1x JanSpiesZA-54-ORP_Sonar_stand-Body.stl

aangeraden vscode extensions:
ROS(optioneel),python,Remote - SSH.

gereedschap en materialen nodig (linkszijn meer voor voorbeelden):
wifi.
1x laptop/pc(i use Ubuntu 22.04.4 LTS for this project).
1x raspberry Pi 4(of met andere Pi`s compatable met ros2,gpiozero,circuitpython,ubuntu server,vscode).
1x micro sd card met ubuntu server os  and ros2 geinstalleert.
2x yellow tt dc motor( je hebt 20 mm jumper wires with m uiteinde  gesoldeert voor gebruik):

https://www.amazon.nl/Dealikee-stuks-motor-transmissiemotor-dubbele/dp/B09BYWXBNC/ref=sr_1_5?crid=31S7WNFDF4YG8&dib=eyJ2IjoiMSJ9.JGnixIX7--Z81XtCUr2_DmykWcrCb87UE2xFxufTjfAeLAs3QvQ6Y9Dlfx--Lrz4_7H2UvXJD59GMDZgMpwp2egi_zcUO1meJPeesPInDIuJ9ICV4GCjF5sNjBiS3cCbEwQ-I8dkJbK2XGH9qOcUZMz1qNJob__rYmYdPyppAHQ7WHwxJclSlYpSzImbKl92WcmMaJp9UZGx9gYoOwGr4xDiVbC-2c8dK_DwOjT39gPz51BI8i3qpfvFdP37B00IVYbVhXCbizMaZNMHgjbxoH8Tvg7A91QgGma1Agdjezk.D8IgTh-zeaNPCvByfphMVOltwUojXmkIH3iLDYMxazs&dib_tag=se&keywords=tt+motor&qid=1715261040&refinements=p_n_free_shipping_eligible%3A17033278031&rnid=17033270031&sprefix=tt+mo%2Caps%2C71&sr=8-5.

1x HC-SR04 Rangefinder Sensor: https://www.amazon.nl/AZDelivery-Ultrasone-compatibel-Rangefinder-Raspberry/dp/B07TKVPPHF/ref=sr_1_2?crid=3FXOXPHM7LYOL&dib=eyJ2IjoiMSJ9.13REM5XZdn_arQn7PKyADHpWvxcamMRy4rSyJ4Iujxi1wYXX98h2O8eEp2zvKKdzixq0XQCEEoSwVKhiOzh1wFa7NSfzM2YaCwWqLl6bI9Emtu3AZnMZY-JAWJEeBMs0VHlulnkDM3acvOuafLIoBq_GjjcC5j2PoYxQ4pI1WBuqqlzn7GwNy7BISKmXogL9RxTW238Ckh8PeBpNusgY0nrpFbkuhT7PiCHIwBnu-TFMTW8QZ9MPft-GYp81QvpDrqZWfH2I1keNXzF_uDOnX4hf9My4tjnn9x-KLOW-Ljs.7JEQcDgc5Dm5ohjIFujg65oZqWluPG_2W4u2mKmnB7E&dib_tag=se&keywords=distance%2Bsensor&qid=1715260894&sprefix=distance%2Caps%2C80&sr=8-2&th=1.
11x f/f 20 mm jumper wire: https://www.tinytronics.nl/en/cables-and-connectors/cables-and-adapters/prototyping-wires/dupont-compatible-and-jumper/dupont-jumper-wire-female-female-20cm-10-wires.
2 x m/f jumper wire 20 mm : https://www.tinytronics.nl/en/cables-and-connectors/cables-and-adapters/prototyping-wires/dupont-compatible-and-jumper/dupont-jumper-wire-male-female-20cm-10-wires.

2x m/m 20mm jumper wire : https://www.tinytronics.nl/en/cables-and-connectors/cables-and-adapters/prototyping-wires/dupont-compatible-and-jumper/dupont-jumper-wire-male-male-20cm-10-wires.

1x  DC Jack Female 5.5mm to Terminal Block: https://www.tinytronics.nl/en/cables-and-connectors/connectors/screw-terminals/dc-jack-female-5.5mm-to-terminal-block.
1x 9V Battery Clip with DC Jack: https://www.tinytronics.nl/nl/power/batterijhouders-en-clips/9v/9v-batterij-clip-met-dc-jack.

1x 9v battery: https://www.tinytronics.nl/en/power/batteries/9v/procell-intense-9v-battery.

1x USB-C USB-A 2.0 Cable - 1m: https://www.tinytronics.nl/en/cables-and-connectors/cables-and-adapters/usb/usb-c/goobay-45735-usb-c-usb-a-2.0-cable-1m-3a-black.

inbussleutel en schroevndraaier(ook m2 maat voor motor driver en DC Jack Female 5.5mm to Terminal Block)en  moeren   voor bouten :
4x 2.5*6mm.
4x m3*8 mm.
12x m3*12 mm.
4x m3*20 mm.
4x m3*30 mm.

