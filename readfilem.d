import std.stdio; 
import std.file; 
 
void main() { 
   File file = File("test.txt", "w+");
   file.writeln("hello");  
   file.close(); 
   file = File("compiled.txt", "r"); 
   
   string s = file.readln(); 
   writeln(s);
   
   file.close(); 
} 