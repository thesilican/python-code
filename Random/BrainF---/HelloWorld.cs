using System;
class Program {
public static void Main(string[] args) {
int[] arr = new int[1000];
int ptr = 0;
        var inc = () => arr[ptr]++;
        inc();
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
while(arr[ptr] != 0) {
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
while(arr[ptr] != 0) {
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
arr[ptr]++;
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
ptr = (ptr + 1 + 1000) %1000;
ptr = (ptr + 1 + 1000) %1000;
ptr = (ptr + 1 + 1000) %1000;
ptr = (ptr + 1 + 1000) %1000;
arr[ptr]--;
}
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]--;
ptr = (ptr - 1 + 1000) %1000;
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
while(arr[ptr] != 0) {
ptr = (ptr + 1 + 1000) %1000;
}
ptr = (ptr + 1 + 1000) %1000;
arr[ptr]--;
}
ptr = (ptr - 1 + 1000) %1000;
ptr = (ptr - 1 + 1000) %1000;
Console.Write((char)arr[ptr]);
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
Console.Write((char)arr[ptr]);
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
Console.Write((char)arr[ptr]);
Console.Write((char)arr[ptr]);
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
Console.Write((char)arr[ptr]);
ptr = (ptr - 1 + 1000) %1000;
ptr = (ptr - 1 + 1000) %1000;
Console.Write((char)arr[ptr]);
ptr = (ptr + 1 + 1000) %1000;
arr[ptr]--;
Console.Write((char)arr[ptr]);
ptr = (ptr + 1 + 1000) %1000;
Console.Write((char)arr[ptr]);
arr[ptr]++;
arr[ptr]++;
arr[ptr]++;
Console.Write((char)arr[ptr]);
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
Console.Write((char)arr[ptr]);
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
arr[ptr]--;
Console.Write((char)arr[ptr]);
ptr = (ptr - 1 + 1000) %1000;
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
Console.Write((char)arr[ptr]);
ptr = (ptr - 1 + 1000) %1000;
arr[ptr]++;
arr[ptr]++;
Console.Write((char)arr[ptr]);
}
}