import std.stdio;
import std.string;

void main() { 
   File file = File("test.txt", "w");  
   file.writeln("hello"); 
   file.writeln("world");  
   file.close();  
   file = File("compiled.txt", "r"); 
    
   while (!file.eof()) { 
      string line = chomp(file.readln()); 
      writeln("line -", line); 
   }
} 