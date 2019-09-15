import java.util.*;
import javafx.util.*;

public class Student
{
   public String name;
   public ArrayList<Subject> studentsSubjects;  //semestre,nota
   
   public Student(String name, ArrayList<Subject> studentsSubjects){
       this.name = name;
       this.studentsSubjects = studentsSubjects;
   }
   
   public String getName(){
        return name;
   }
    
   public ArrayList<Subject> getSubjects(){
        return studentsSubjects;
   }
}
