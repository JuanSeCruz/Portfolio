close all; clear all; clc
ind=1; fi=35*pi/180;
space_color='k';
npanels=60; 
alpha   = 1; 
GMST0 = 4.89496121282306; 
image_file = 'tierra.jpg';
cdata = imread(image_file);
continentes;     

erad    = 2;
prad    = 2;
erot    = 7.2921158553e-5;
for ii=1:6
    for jj=1:4
        theta=ii*60*pi/180;
        a=[cos(theta)*cos(fi),sin(theta)*cos(fi),sin(fi)];
        i=cross([0 0 1],a);
        i=i/norm(i);
        j=cross(a,i);
        j=j/norm(j);
        a0=jj*pi/2+rand*0.2;
        temp.a=a;
        temp.i=i;
        temp.j=j;
        temp.a0=a0;
        sat(ind)=temp;
        ind=ind+1;
    end
end
w=2*pi/0.070; R=10;
[Xt, Yt, Zt] = ellipsoid(0, 0, 0, erad, erad, prad, npanels);
Xt=Xt*R/3; Yt=Yt*R/3; Zt=Zt*R/3;
Rt=R/3;
Lat=6*pi/180;
Lon=-75*pi/180;
Ro=Rt*[cos(Lon)*cos(Lat),sin(Lon)*cos(Lat),sin(Lat)];
Io=[sin(Lon),-cos(Lon),0];
Ko=-Ro/Rt;
i=1;
Jo=cross(Ko,Io);

for t=0:0.1:100
    ang=w*t;
    
    for k=1:24
        x=R*cos(ang+sat(k).a0);
        y=R*sin(ang+sat(k).a0);
        r=x*sat(k).i+y*sat(k).j;
        Xr=dot(r-Ro,Io);
        Yr=dot(r-Ro,Jo);
        Zr=dot(r-Ro,Ko);
        lngh(k)=atan2(r(2),r(1))';
        ltt(k)=asin(r(3)/R);
        ax=subplot(2,2,1);
        if(Zr<0)
            plot3(r(1),r(2),r(3),'.w','markerFacecolor',[0 0 0]);
        else 
            plot3(r(1),r(2),r(3),'.b','markerFacecolor',[0 0 0]);
        end
        hold on;
        subplot(2,1,2);
        
        
        if(Zr<0)
            plot(Xr,Yr,'pr');hold on;
        end
        az=subplot(2,2,2);
        plot(america(:,1)*180/pi, america(:,2)*180/pi,'linewidth',2); hold on;
        plot(europa(:,1)*180/pi, europa(:,2)*180/pi,'linewidth',2); hold on;
        plot(africa(:,1)*180/pi, africa(:,2)*180/pi,'linewidth',2); hold on;
        plot(australia(:,1)*180/pi, australia(:,2)*180/pi,'linewidth',2); hold on;
        plot(lngh(k)*180/pi,ltt(k)*180/pi,'.w'); 
        set(az,'color',[1 1 1]*0.2);
        hold on;
         
    end
    subplot(2,1,2);
    theta=0:0.01:2*pi;
    E=2*cos(theta);
    I=2*sin(theta);
    plot(E,I,'-b');
    E1=10*cos(theta);
    I2=10*sin(theta);
    plot(E1,I2,'-b'); hold on;
    subplot(2,2,1);
     set(ax,'color',[0 0 0]);
     globe = surf(Xt, Yt, -Zt, 'FaceColor', 'none', 'EdgeColor', 0.5*[1 1 1]);
     set(globe, 'FaceColor', 'texturemap', 'CData', cdata, 'FaceAlpha', alpha, 'EdgeColor', 'none');
     rotate(globe,[0 0 1],ang/6);
     subplot(2,2,1);
     axis equal;
     axis([-R R -R R -R R]);
     hold off;
     subplot(2,2,2);
     axis ([-180 180 -90 90]);
     hold off;
     subplot(2,1,2);
     axis equal;
     axis([-R R -R R]);
     hold off;
    pause(0.01)
    
end