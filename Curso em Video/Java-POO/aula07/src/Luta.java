import java.util.Random;

// Relacionamento ou Agregação entre classes, aula 08
//Explicação: com os dois objetos da classe Lutador fazemos um relacionamento com 
//os metodos que serão criados nessa nova classe, Luta.
public class Luta {
    // Atributos
    private Lutador desafiado;
    private Lutador desafiante;
    private int rounds;
    private boolean aprovada;

    //Métodos Públicos
    public void marcarLuta(Lutador l1, Lutador l2) {
        if ( l1.getCategoria().equals(l2.getCategoria())    // SE A CATEGORIA DO L1 FOR IGUAL A CATEGORIA DO L2
                && l1 != l2){                               // E SE O LUTADOR 1 FOR DIFERENTE DE LUTADOR 2                
                    this.aprovada = true;
                    this.desafiado = l1;
                    this.desafiante = l2;
                }else {
                    this.aprovada = false;
                    this.desafiado = null;
                    this.desafiante = null;
                }
    }
    public void lutar(){
        if (this.aprovada){
            System.out.println("### DESAFIADO ###");
            this.desafiado.apresentar();
            System.out.println("### DESAFIANTE ###");
            this.desafiante.apresentar();

            Random aleatorio = new Random();
            int vencedor = aleatorio.nextInt(3); // 0 1 2
            System.out.println("====== RESULTADO ======");
            switch(vencedor){
                case 0:// Empate
                    System.out.println("Empate!");
                    this.desafiado.empatarLuta();
                    this.desafiante.empatarLuta();
                    break;

                case 1:// Desafiado vence
                    System.out.println("Vitória do " + this.desafiado.getNome(null));
                    this.desafiado.ganharLuta();
                    this.desafiante.perderLuta();

                case 2://Desafiante vence 
                    System.out.println("Vitória do " + this.desafiante.getNome(null));
                    this.desafiante.ganharLuta();
                    this.desafiado.perderLuta();
            }
        }else{
            System.out.println("A luta não pode acontecer!");
        }
        System.out.println("======================");
    }
    //Métodos Especiais
    public Lutador getDesafiado(){
        return desafiado;
    }
    public void setDesafiado(Lutador desafiado){
        this.desafiado = desafiado;
    } 


    public Lutador getDesafiante(){
        return desafiante;
    }
    public void setDesafiante(Lutador desafiante){
        this.desafiante=desafiante;
    }


    public int getRounds(){
        return rounds;
    }
    public void setRounds(int rounds){
        this.rounds = rounds;
    }


    public boolean getAprovada(){
        return aprovada;
    }
    public void setAprovada( boolean aprovada){
        this.aprovada = aprovada;
    }

}
