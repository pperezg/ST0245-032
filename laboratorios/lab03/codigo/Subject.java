import java.util.*;


public class Subject
{
    public static String Scode;
    public static int grade;
    public int sSemester;
    
    public Subject(String Scode, int grade,int sSemester)
    {
        this.Scode = Scode;
        this.grade = grade;
        this.sSemester = sSemester;
    }
    
    public String getCode(){
        return this.Scode;
    }
    
    public int getGrade(){
        return this.grade;
    }
    
    public int getSemester(){
        return this.sSemester;
    }
}
