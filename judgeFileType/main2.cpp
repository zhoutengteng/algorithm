#include <fstream>  
#include <iostream>
using namespace std;  
  

/**
 *记事本打开txt文件，然后另存，有四种编码格式可供选择,分别是:
 *ANSI                    无格式定义                      对于中文编码格式是GB2312;
 *Unicode                 文本里前两个字节为FF FE          字节流是little endian
 *Unicode  big endian     文本里前两个字节为FE FF          字节流是big  endian
 *UTF-8                   前两字节为EF BB，第三字节为BF     带bom
 * 
 */


bool IsUTF8(const void* pBuffer, long size)   
{   
    bool IsUTF8 = true;   
    unsigned char* start = (unsigned char*)pBuffer;   
    unsigned char* end = (unsigned char*)pBuffer + size;   
    while (start < end)   
    {   
        if (*start < 0x80) // (10000000): 值小于0x80的为ASCII字符   
        {   
            start++;   
        }   
        else if (*start < (0xC0)) // (11000000): 值介于0x80与0xC0之间的为无效UTF-8字符   
        {   
            IsUTF8 = false;   
            break;   
        }   
        else if (*start < (0xE0)) // (11100000): 此范围内为2字节UTF-8字符   
        {   
            if (start >= end - 1)    
                break;   
            if ((start[1] & (0xC0)) != 0x80)   
            {   
                IsUTF8 = false;   
                break;   
            }   
            start += 2;   
        }    
        else if (*start < (0xF0)) // (11110000): 此范围内为3字节UTF-8字符   
        {   
            if (start >= end - 2)    
                break;   
            if ((start[1] & (0xC0)) != 0x80 || (start[2] & (0xC0)) != 0x80)   
            {   
                IsUTF8 = false;   
                break;   
            }   
            start += 3;   
        }    
        else  
        {   
            IsUTF8 = false;   
            break;   
        }   
    }   
    return IsUTF8;   
}  



int main(int argc, char* argv[]) {  
    ifstream fin(argv[1],ios::binary);  
    unsigned char  s2;  
    fin.read((char*)&s2, sizeof(s2));//读取第一个字节，然后左移8位  
    int p = s2<<8;  
    fin.read((char*)&s2, sizeof(s2));//读取第二个字节  
    p +=s2;  
  
    string code;  
  
    switch(p)//判断文本前两个字节  
    {  
    case 0xfffe:  //65534  
        code = "Unicode";      
        break;  
    case 0xfeff://65279  
        code = "Unicode big endian";  
        break;  
    case 0xefbb://61371  
        code = "UTF-8";       
        break;  
    default:   
        code = "ANSI";   
     }
     cout << code << endl;
     fin.close();   
     return 0;  
}  

