import java.util.List;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElementWrapper;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAccessType;



@XmlAccessorType(XmlAccessType.FIELD)
@XmlRootElement(name="department")
public class Department {

    @XmlAttribute
    private String name;    //部门名称

    @XmlElement(name="staff")
    private List<Staff> staffs;           // 其实staff是单复同型，这里是加's'是为了区别staff

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public List<Staff> getStaffs() {
        return staffs;
    }
    public void setStaffs(List<Staff> staffs) {
        this.staffs = staffs;
    }

    public String toString() {
        StringBuilder sb=new StringBuilder();
        for(Staff staff:staffs){
            sb.append(staff.toString());
        }
        return sb.toString();
    }

}
