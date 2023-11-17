

public class Caneta {
    public String modelo;
    private float ponta;
    private String cor;
    private boolean tampada;


    public Caneta(String m,  String c, float p ) { // este é o metpdp construtor
        this.modelo = m;
        this.cor = c;
        this.ponta = p;
        this.tampar();
        

    }

    public String getModelo(String m){
        return this.modelo;
    }
    public void setModelo(String m){
        this.modelo=m;
    }
    public float getPonta(){
        return this.ponta;
    }
    public void setModelo(float p){
        this.ponta=p;
    }

    public void tampar(){
        this.tampada = true;
    }
    public void destampar(){
        this.tampada = false;
    }

    public void status(){
        System.out.println("SOBRE A CANETA: ");
        System.out.println("Modelo: " + getModelo(modelo));
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Cor: " + this.cor);
        System.out.println("Tampada: " + this.tampada);
    }
    public void setPonta(float f) {
    }
}
