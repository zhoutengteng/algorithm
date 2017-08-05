import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ByteArrayOutputStream;
import java.io.StringWriter;
import java.util.ArrayList;
import java.util.List;

public class Xml2obj {

    public static void main(String[] args) throws Exception {

        JAXBContext context = JAXBContext.newInstance(Department.class,Staff.class);    // 获取上下文对象
        Marshaller marshaller = context.createMarshaller(); // 根据上下文获取marshaller对象

        marshaller.setProperty(Marshaller.JAXB_ENCODING, "UTF-8");  // 设置编码字符集
        marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true); // 格式化XML输出，有分行和缩进
        marshaller.marshal(getSimpleDepartment(),System.out);   // 打印到控制台

        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        marshaller.marshal(getSimpleDepartment(), baos);
        String xmlObj = new String(baos.toByteArray());         // 生成XML字符串
        System.out.println(xmlObj);



        JAXBContext context2 = JAXBContext.newInstance(Department.class);
        Unmarshaller unmarshaller = context.createUnmarshaller();
        Department root = (Department)unmarshaller.unmarshal(new File("xml.xml"));
        System.out.println(root.toString());

    }

    /**
     * 生成一个简单的Department对象
     * @return
     */
    private static Department getSimpleDepartment() {
        List<Staff> staffs = new ArrayList<Staff>();

        Staff stf = new Staff();
        stf.setName("周杰伦");
        stf.setAge(30);
        stf.setSmoker(false);
        staffs.add(stf);
        stf.setName("周笔畅");
        stf.setAge(28);
        stf.setSmoker(false);
        staffs.add(stf);
        stf.setName("周星驰");
        stf.setAge(40);
        stf.setSmoker(true);
        staffs.add(stf);

        Department dept = new Department();
        dept.setName("娱乐圈");
        dept.setStaffs(staffs);

        return dept;
    }
}
