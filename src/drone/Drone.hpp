#ifndef DRONE_H
#define DRONE_H

#include "Bateria.hpp"
#include <string>
using namespace std;

class Drone{
    public:
        Drone(string nome, Bateria* bateria, double posicao);
        virtual ~Drone();

        void takeoff(int altura);
        void land();
        bool setPosition(double x, double y);
        double getPosicao();
        double getAltura();
        Bateria *getBateria();
        virtual bool mapear();
        void status();
};

#endif
