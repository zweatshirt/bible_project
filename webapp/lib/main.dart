import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';
import 'package:firebase_database/firebase_database.dart';
import 'views/home.dart';


void main() async {
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(const BibleApp()); 
}



class BibleApp extends StatefulWidget {
  const BibleApp({super.key});
  @override
  State<BibleApp> createState() => _BibleAppState();

}

class _BibleAppState extends State<BibleApp> {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'KJVBibleReader.com',
      theme: ThemeData(
          useMaterial3: true,
          colorScheme: ColorScheme.fromSeed(
            seedColor: Colors.white,
            brightness: Brightness.dark,
          ),
        
      ),
      home: const Home(),
    );
  }
}
