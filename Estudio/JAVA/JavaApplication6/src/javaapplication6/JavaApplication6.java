/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javaapplication6;

/**
 *
 * @author Flia Cadenacevedo
 */
public class JavaApplication6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int mes=8;
        
        switch(mes){
            case 1,3,5:
                System.out.println("mes de 31");
                break;
            case 2:
                System.out.println("mes de 28");
            case 4,6,8:
                System.out.println("mes de 30");
                break;
               
        }
    }
    
}
