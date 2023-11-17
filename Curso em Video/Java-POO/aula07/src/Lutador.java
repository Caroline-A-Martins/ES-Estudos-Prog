public class Lutador {
    private String nome, nacionalidade, categoria;
    private int idade, vitorias, derrotas, empates;
    private float altura, peso;


    public void apresentar(){
        System.out.println("---------------------------");    
        System.out.println("CHEGOU A HORA! Apresentamos o lutador " + this.getNome(nome));
        System.out.println("Diretamente de " + this.getNacionalidade(nacionalidade));
        System.out.println("com " + this.getIdade(idade) + " anos e " + this.getAltura(altura) + "");    
        System.out.println("pesando " + this.getPeso(peso) + "Kg");   
        System.out.println(this.getVitorias(vitorias) + " vitórias");
        System.out.println(getDerrotas(derrotas) + " derrotas " );
        System.out.println(this.getEmpates(empates) + " empates!");
        
    }

    public void status(){
        System.out.println(this.getNome(nome) + " é um peso " + this.getCategoria());
        System.out.println("Ganhou " + this.getVitorias(vitorias) + " vezes");
        System.out.println("Perdeu " + this.getDerrotas(derrotas) + " vezes");
        System.out.println("Empatou " + this.getEmpates(empates) + " vezes");
        
    }

    public void ganharLuta() {
        //this.setVitorias(this.getVitorias() + 1);
        this.vitorias = this.vitorias + 1;
    }

    public void perderLuta() {
        //this.setDerrotas(this.getDerrotas() + 1);
        this.derrotas = this.derrotas + 1;
    }

    public void empatarLuta() {
        this.empates = this.empates + 1;

    }

    public Lutador(String no, String na, int i, float al, float pe, int vi, int de, int em ){ 
        this.nome = no;
        this.nacionalidade = na;
        this.idade = i ; 
        this.altura = al;
        this.setPeso(pe);;
        this.vitorias = vi;
        this.derrotas = de;
        this.empates = em;  
        
    }

    public String getNome(String nome){
        return this.nome;
    }
    public void setNome(String nome){
        this.nome=nome;
    }


    public String getNacionalidade(String nacionalidade){
        return this.nacionalidade;
    }
    public void setNacionalidade(String nacionalidade){
        this.nacionalidade = nacionalidade;
    }


    public int getIdade(int idade){
        return this.idade;
    }
    public void setIdade(int idade){
        this.idade = idade;
    }


    public float getAltura(float altura){
        return this.altura;
    }
    public void setAltura(float altura){
        this.altura = altura;
    }

    
    public float getPeso(float peso){
        return this.peso;
    }
    public void setPeso(float peso){
        this.peso = peso;
        this.setCategoria();
    }
    

    public String getCategoria(){
        return categoria;
    }
    
    private void setCategoria(){
        if ( this.peso < 52.2){
            this.categoria = "Invalido";
        }else if (this.peso <= 70.3){
            this.categoria = "Leve";
        }else if (this.peso <= 83.9){
            this.categoria = "Médio";
        }else if(this.peso < 120.2){
            this.categoria = "Pesado";
        }else {
            this.categoria = "Invalido";
        }
    }


    public int getVitorias(int vitorias){ 
        return this.vitorias;
    }
    public void setVitorias(int vitorias){
        this.vitorias = vitorias;
    }


    public int getDerrotas(int derrotas){ 
        return this.derrotas;
    }
    public void setDerrotas(int derrotas){
        this.derrotas = derrotas;
    }


    public int getEmpates(int empates){ 
        return this.empates;
    }
    public void setEmpates(int empates){
        this.empates = empates;
    }

}

 