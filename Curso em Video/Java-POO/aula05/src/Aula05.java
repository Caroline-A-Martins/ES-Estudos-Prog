import aula05.ContaBanco;

public class Aula05 {
    public static void main(String[] args) {
        ContaBanco p1 = new ContaBanco();
        p1.setNumConta(1111);
        p1.setDono("Carlos");
        p1.setTipo("CC");

        ContaBanco p2 = new ContaBanco();
        p2.setNumConta(2222);
        p2.setDono("Ana");
        p2.setTipo("PC");

        p1.depositar(100);
        p2.depositar(500);
        p2.sacar(100);


        p1.estadoAtual();
        p2.estadoAtual();
        
    }
}
