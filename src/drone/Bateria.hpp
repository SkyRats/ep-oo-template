#ifndef BATERIA_H
#define BATERIA_H

class Bateria{
    public:
        Bateria(int mah, int tempoDeCarregamento);
        ~Bateria();
        bool carregar(int tempo);
        bool usar(int tempo);
        int getMah();
        int getCarga();
        int calculaTempoDeVoo();
        int getTempoDeCarregamento();
        void status();
};

#endif
