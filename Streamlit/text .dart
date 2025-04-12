import 'package:flutter/material.dart';

// function to trigger build process
void main() => runApp(const GeeksforGeeks());

class GeeksforGeeks extends StatelessWidget { const GeeksforGeeks({Key? key}) : super(key: key);

@override
Widget build(BuildContext context) { return MaterialApp(

8
 

home: Scaffold(
backgroundColor: Colors.lightGreen, appBar: AppBar(
backgroundColor: Colors.green, title: const Text("welcome Screen"),
), // AppBar body: Container(
child: const Center(
child: Text("Hello world!!"),
), // Center
), // Container
), // Scaffold
); // MaterialApp
}
}
