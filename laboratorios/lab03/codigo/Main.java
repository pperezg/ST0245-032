import java.util.*;
import java.io.*;
import javafx.util.*;
import java.lang.reflect.Array;

public class Main
{
    public ArrayList<Subject> subjectsList = new ArrayList<>();
    public static String DataDoc;
    public static ArrayList<Student> studentsList = new ArrayList<>();
    
    public static void ReadFile(){
        try{
            System.out.println("Enter the file's name with its extension.");
            Scanner scn1 = new Scanner(System.in);
            DataDoc = scn1.nextLine();
            
            Scanner savedData = new Scanner(new File(DataDoc));
            savedData.nextLine();
            savedData.nextLine();
            ArrayList<String[]> p = new ArrayList();
            while (savedData.hasNextLine()){
                String line = savedData.nextLine();
                String[] divided = line.split(",");
                p.add(divided);
                if (savedData.hasNextLine()){
                    savedData.nextLine();
                }
            }
            String StName = (String)Array.get(p.get(0),0);
            String SjCode = (String)Array.get(p.get(0),2);
            int SjSemester = Integer.parseInt((String)Array.get(p.get(0),3));
            int SjGrade = Integer.parseInt((String)Array.get(p.get(0),13));
            ArrayList<Subject> subj = new ArrayList();
            Subject s1 = new Subject(SjCode,SjGrade,SjSemester);
            subj.add(s1);
            for(String[] j : p){
                if(!j[0].equals(StName)){
                    Student s = new Student(StName, subj);
                    studentsList.add(s);
                    StName = j[0];
                    SjCode = j[2];
                    SjSemester = Integer.parseInt(j[3]);
                    SjGrade = Integer.parseInt(j[13]);
                    subj.clear();
                    Subject s2 = new Subject(SjCode,SjGrade,SjSemester);
                    subj.add(s2);
                } else if(!j[2].equals(SjCode)){
                    SjCode = j[2];
                    SjSemester = Integer.parseInt(j[3]);
                    SjGrade = Integer.parseInt(j[14]);
                    Subject s3 = new Subject(SjCode,SjGrade,SjSemester);
                    subj.add(s3);
                }
            }
        } catch (FileNotFoundException e){
            System.out.println("Said file wasn't found, please try again.");
        }
    }
    
    public static void Choice1(){
        System.out.println("Which subject do you want to search for?");
        Scanner scn3 = new Scanner(System.in);
        String desiredSubject = scn3.nextLine();
        
        System.out.println("Which semester of the said subject are you looking for?");
        Scanner scn4 = new Scanner(System.in);
        int desiredSemester = Integer.parseInt(scn4.nextLine());
        
        for(Student st: studentsList){
            for (Subject sbj: st.studentsSubjects){
                if(sbj.Scode.equals(desiredSubject) && sbj.sSemester==desiredSemester){
                    System.out.println("Student:"+ st.name + " Grade:" + sbj.grade);
                }
            }
        }
    }
    
    public static void Choice2(){
        System.out.println("Which student do you want to search for?");
        Scanner scn5 = new Scanner(System.in);
        String desiredStudent = scn5.nextLine();
        
        System.out.println("Which semester are you looking for?");
        Scanner scn6 = new Scanner(System.in);
        int desiredSemester2 = Integer.parseInt(scn6.nextLine());
        
        for(Student st: studentsList){
            if(st.name.equals(desiredStudent)){
                for (Subject sbj: st.studentsSubjects){
                    if(sbj.sSemester==desiredSemester2){
                        System.out.println("Subject:"+ sbj.Scode + " Grade:" + sbj.grade);
                    }
                }
            }
        }
    }
    
    public static void main(){
        System.out.println("Enter the type of search you want to realize (1 / 2)");
        Scanner scn2 = new Scanner(System.in);
        int choice = Integer.parseInt(scn2.nextLine());
        if(choice == 1){
            ReadFile();
            Choice1();
        } else if (choice == 2){
            ReadFile();
            Choice2();
        }
    }
}
