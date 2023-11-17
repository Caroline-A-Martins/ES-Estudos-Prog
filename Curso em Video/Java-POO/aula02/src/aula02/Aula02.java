package aula02;
public class Aula02 {
    public static void main(String[] args) throws Exception {
        Caneta c1 = new Caneta();
        System.out.println("Caneta 1");
        c1.cor = "cor";
        c1.ponta = 0.5f;
        c1.tampar();
        c1.status();
        c1.rabiscar();

        Caneta c2 = new Caneta();
        System.out.println("Caneta 2");
        c2.cor = "vermelha";
        c2.ponta = 0.7f;
        c2.destampar();
        c2.status();
        c2.rabiscar();

            
        }
}
