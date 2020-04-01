% Mohammad Safeea, 1st-April-2020
% testing the joystick

%% Initiation
close all;clear all;clc;
%% Start joystick
ID=1;
joy=vrjoystick(ID);
c = caps(joy) ;
disp(c)
%% Read loop
while true
    [axes,buttons,pov]=read(joy)
%     buttonStatus=button(joy)
    pause(0.2);
end
close(joy);