
/*
    功能：实现文件编码格式的判断
    通过一个文件的最前面三个字节，可以判断出该的编码类型：
    ANSI：　　　　　　　　无格式定义；(第一个字节开始就是文件内容)
    Unicode： 　　　　　　前两个字节为FFFE；
    Unicode big endian：　前两字节为FEFF；　 
    UTF-8：　 　　　　　　前两字节为EFBB，第三字节为BF
*/
 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
// 读取一个文件的最前面n个字节，并以十六进制形式输出每个字节的值
void readNBytes(char *fileName, int n)
{
    FILE *fp = fopen(fileName, "r");
    unsigned char *buf = (unsigned char*)malloc(sizeof(unsigned char)*n);
    int i;
    if(fp == NULL)
    {
        printf("open file [%s] failed.\n", fileName);
        return;
    }
    fread(buf, sizeof(unsigned char), n, fp);
    fclose(fp);
    
    for(i = 0; i < n; i++)
    {
        printf("%x\t", buf[i]);
    }
    printf("%s:\t", fileName); 
    printf("\n");
    free(buf);
}

void creatUTF8file() {
    char header[3] = {0xef, 0xbb, 0xbf};  // UTF-8 file header
    FILE * fp = fopen("utf8.txt", "w+b");
    fwrite(header, sizeof(char), 3, fp);
    /* 在UTF-8文件头部之后写入其他信息 */
    char line[] ={0xE4,0xB8,0x81, 0xe4, 0xb8, 0x80};
    fwrite(line, sizeof(char), 6, fp);
    fclose(fp);
}

void creatUnicodeLittleEnddianfile() {
    char header[3] = {0xff, 0xfe};  // UTF-16 === unicode file header
    FILE * fp = fopen("unicodeLittleEndian.txt", "w+b");
    fwrite(header, sizeof(char), 2, fp);
    /* 在UTF-8文件头部之后写入其他信息 */
    char line[] ={0x01,0x4e,0x00,0x4e};
    fwrite(line, sizeof(char), 4, fp);
    fclose(fp);
}

void creatUnicodeBigEnddianfile() {
    char header[3] = {0xfe, 0xff};  // UTF-16 === unicode file header
    FILE * fp = fopen("unicodeBigEndian.txt", "w+b");
    fwrite(header, sizeof(char), 2, fp);
    /* 在UTF-8文件头部之后写入其他信息 */
    char line[] ={0x4e,0x01,0x4e,0x00};
    fwrite(line, sizeof(char), 4, fp);
    fclose(fp);
}

void creatGBKfile() {
    char header[3] = {0xfe, 0xff};  // UTF-16 === unicode file header
    FILE * fp = fopen("gbk.txt", "w+b");
    //fwrite(header, sizeof(char), 2, fp);
    /* 在UTF-8文件头部之后写入其他信息 */
    char line[] ={0xb6,0xa1,0xd2,0xbb};
    fwrite(line, sizeof(char), 4, fp);
    fclose(fp);
}
    

 
int main(int argc, char* argv[]) {
    if (argc >= 2) {
        int ishas = false;
        for (int i = 0; i < argc; i++) {
            if (strcmp(argv[i], "-write") == 0 | strcmp(argv[i], "-test") == 0) {
                ishas = true;
            }
        }
        if (!ishas) {
           printf("please intput parameter -write or -test\n");
        }
    } else {
        printf("please intput parameter -write or -test\n");
    }

    for (int i = 0; i < argc; i++) {
        if (strcmp(argv[i], "-write") == 0) {
            creatUTF8file();
            creatUnicodeLittleEnddianfile();
            creatUnicodeBigEnddianfile();
            creatGBKfile();
        }
    }
    for (int i = 0; i < argc; i++) {
        if (strcmp(argv[i], "-test") == 0) {
            char fileName[][50] = {"ansi.txt", "unicodeBigEndian.txt", "unicodeLittleEndian.txt", "utf8.txt", "gbk.txt"};
            int i;
            for(i = 0; i < 5; i++) {
                // 每个文件中的内容都是：你what123456
                readNBytes(fileName[i], 12);
            }
        }
    }
   return 0;
}