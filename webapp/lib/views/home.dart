import 'dart:math';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:kjv/widgets/app_bar/my_app_bar.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:firebase_core/firebase_core.dart';

List<String> titles = <String>[
  'Book',
  'Chapter',
  'Verse Search',
  'Dictionary',
];

class Home extends StatefulWidget {
  final Future<FirebaseApp> firebaseApp;
  const Home({super.key, required this.firebaseApp});
  

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {


  @override
  Widget build(BuildContext context) {
    final ColorScheme colorScheme = Theme.of(context).colorScheme;
    final Color oddItemColor = colorScheme.primary.withOpacity(0.05);
    final Color evenItemColor = colorScheme.primary.withOpacity(0.10);
    const int tabsCount = 4;

    // Update this method, which is intended to grab data from the rt db
    Future<List<String>?> getData() async {
       await Future.delayed(
        const Duration(seconds: 2)
       );
    
      return ["Temp list val"];
    }


    return DefaultTabController(
      initialIndex: 0,
      length: tabsCount,
      child: Scaffold(
        appBar: MyAppBar(),

        body: 
                
        TabBarView(
          
          children:
            // FutureBuilder(
            //   future: _
            // ),

           <Widget>[
            // Books view
            Container(
              child: 
                FutureBuilder(
                  future: getData(),
                  builder: (context, snapshot) {
                    if (snapshot.hasError) {
                      print("Error: ${snapshot.error.toString()}");
                      return const Text('Something went wrong!');
                    }
                    else if (snapshot.hasData) {
                      print('Successful call!');
                      return ListTile(
                        // tileColor: index.isOdd ? oddItemColor : evenItemColor,
                        tileColor: evenItemColor,
                        title: const Text('meep'),
                        hoverColor: colorScheme.primary.withOpacity(1),
                        focusColor: oddItemColor,

                      );
                    }
                    else {
                       return const Center(
                        child:  CircularProgressIndicator()
                      );
                    }
                  
                  }

                ),
            ),
            // Chapters view
            Container(
              child: 
                FutureBuilder(
                  future: getData(),
                  builder: (context, snapshot) {
                    if (snapshot.hasError) {
                      print("Error: ${snapshot.error.toString()}");
                      return const Text('Something went wrong two!');
                    }
                    else if (snapshot.hasData &&
                             snapshot.connectionState == ConnectionState.done) {
                      return ListView.builder(
                        itemCount: snapshot.data!.length,
                        itemBuilder: (context, index) {
                          return Text(snapshot.data?[index] ?? "Null value");  
                        });
                    }
                    else {
                       return const Center(
                        child:  CircularProgressIndicator()
                      );
                    }
                  
                  }

                ),
            ),
            // Verse search view
            Container(
              child: 
                FutureBuilder(
                  future: getData(),
                  builder: (context, snapshot) {
                    if (snapshot.hasError) {
                      print("Error: ${snapshot.error.toString()}");
                      return const Text('Something went wrong two!');
                    }
                    else if (snapshot.hasData &&
                             snapshot.connectionState == ConnectionState.done) {
                      return ListView.builder(
                        itemCount: snapshot.data!.length,
                        itemBuilder: (context, index) {
                          return Text(snapshot.data?[index] ?? "Null value");  
                        });
                    }
                    else {
                       return const Center(
                        child:  CircularProgressIndicator()
                      );
                    }
                  
                  }

                ),
            ),
            // Dictionary view
            Container(
              child: 
                FutureBuilder(
                  future: getData(),
                  builder: (context, snapshot) {
                    if (snapshot.hasError) {
                      print("Error: ${snapshot.error.toString()}");
                      return const Text('Something went wrong two!');
                    }
                    else if (snapshot.hasData &&
                             snapshot.connectionState == ConnectionState.done) {
                      return ListView.builder(
                        itemCount: snapshot.data!.length,
                        itemBuilder: (context, index) {
                          return Text(snapshot.data?[index] ?? "Null value");
                        });
                    }
                    else {
                       return const Center(
                        child:  CircularProgressIndicator()
                      );
                    }
                  
                  }

                ),
            ),

          //   ListView.builder(
          //     itemCount: 25,
            
          //     itemBuilder: (BuildContext context, int index) {
                
          //     },
          //   ),
          //   ListView.builder(
          //     itemCount: 25,
          //     itemBuilder: (BuildContext context, int index) {
          //       return ListTile(
          //         // tileColor: index.isOdd ? oddItemColor,
          //         tileColor: oddItemColor,
          //         title: Text('${titles[1]} $index'),
          //       );
          //     },
          //   ),
          //   ListView.builder(
          //     itemCount: 25,
          //     itemBuilder: (BuildContext context, int index) {
          //       return ListTile(
          //         // tileColor: index.isOdd ? oddItemColor : evenItemColor,
          //         tileColor: oddItemColor,
          //         title: Text('${titles[2]} $index'),
          //       );
          //     },
          //   ),
          //   ListView.builder(
          //     itemCount: 25,
          //     itemBuilder: (BuildContext context, int index) {
          //       return ListTile(
          //         // tileColor: index.isOdd ? oddItemColor : evenItemColor,
          //         tileColor: oddItemColor,
          //         title: Text('${titles[3]} $index'),
          //       );
          //     },
          //   ),
          ],
          
        ),
      ),
    );
  }
}