% Mohammad Safeea, 1st-April-2020
% Controlling servos through joystick

%% Initiation
close all;clear all;clc;
instrreset;
%% Start joystick
ID=1;
joy=vrjoystick(ID);
c = caps(joy) ;
disp(c)
%% Start serial
s=serial('COM4');
fopen(s);
%% Read loop
while true
    [axes,buttons,pov]=read(joy);
    angle=(axes(3)+1)*90; % from 0 to 180 degrees
    fwrite(s,angle);
%     buttonStatus=button(joy)
    pause(0.2);
end
close(joy);