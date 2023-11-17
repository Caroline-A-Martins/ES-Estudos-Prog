
package aula11;
public class Aula11 {
    public static void main(String[] args) {
       Visitante v1 = new Visitante();
       v1.setNome("Juvenal");
       v1.setIdade(22);
       v1.setSexo("M");
       System.out.println(v1.toString());
       
       Professor p1 = new Professor();
       p1.setNome("Adriana");
       p1.setIdade(43);
       p1.setSexo("F");
       p1.setEspecialidade("Matematica");
       p1.setSalario(2500.75f);
       System.out.println(p1.toString());
       
       Aluno a1 = new Aluno();
       a1.setNome("Maria");
       a1.setMatricula(111);
       a1.setCurso("Informática");
       a1.setIdade(15);
       a1.setSexo("F");
       System.out.println(a1.toString());
       a1.pagarMensalidade();
       
       Bolsistas b1 = new Bolsistas();
       b1.setNome("Pedro");
       b1.setMatricula(1112);
       b1.setBolsa(12.5f);
       b1.setIdade(17);
       b1.setSexo("M");
       System.out.println(b1.toString());
       b1.pagarMensalidade();
       
       Tecnico t1 = new Tecnico();
       t1.setNome("Ana");
       t1.setRegistroProfissional(222);
       t1.setIdade(24);
       b1.setSexo("F");
       System.out.println(t1.toString());
       t1.praticar();
       
        
    }
    
}
