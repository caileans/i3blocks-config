

#ifndef qtDropDownTemp_h
#define qtDropDownTemp_h

// #include <QApplication>
#include <QtCore>
#include <QtGui>
#include <QWidget>
#include <QDialog> 


enum Justification {
    center,
    right,
    left
};

class QtDropDown: public QDialog {
    private:
        int _borderSize, 
        _bottomBorderLeft, 
        _bottomBorderRight;
        char _borderColor[8],
        _secondBorderColor[8],
        _secondBorderSize[8];
        Justification _justified;
        Q_OBJECT

    public:
        void QtDropDown(const int, const int, const int,Justification, char * , char *, const int, char *, const int, QDialog *parent = 0);
    
    private:
        void paintEvent(event);
        
        void addContent(contentLayout);

        void reposition();

};

//endif