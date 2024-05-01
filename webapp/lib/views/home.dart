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

class Home extends StatelessWidget {

  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    final ColorScheme colorScheme = Theme.of(context).colorScheme;
    final Color oddItemColor = colorScheme.primary.withOpacity(0.05);
    final Color evenItemColor = colorScheme.primary.withOpacity(0.10);
    const int tabsCount = 4;
  

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
            // Container(
            //   child: 
            //     FutureBuilder<QuerySnapshot>(
            //       future: FirebaseDatabase.instance.ref("0").child("0"), builder: (snapshot)
            //     ),
            // ),

            ListView.builder(
              itemCount: 25,
            
              itemBuilder: (BuildContext context, int index) {
                return ListTile(
                  // tileColor: index.isOdd ? oddItemColor : evenItemColor,
                  tileColor: evenItemColor,
                  title: const Text('meep'),
                  hoverColor: colorScheme.primary.withOpacity(1),
                  focusColor: oddItemColor,
                  
                );
              },
            ),
            ListView.builder(
              itemCount: 25,
              itemBuilder: (BuildContext context, int index) {
                return ListTile(
                  // tileColor: index.isOdd ? oddItemColor,
                  tileColor: oddItemColor,
                  title: Text('${titles[1]} $index'),
                );
              },
            ),
            ListView.builder(
              itemCount: 25,
              itemBuilder: (BuildContext context, int index) {
                return ListTile(
                  // tileColor: index.isOdd ? oddItemColor : evenItemColor,
                  tileColor: oddItemColor,
                  title: Text('${titles[2]} $index'),
                );
              },
            ),
            ListView.builder(
              itemCount: 25,
              itemBuilder: (BuildContext context, int index) {
                return ListTile(
                  // tileColor: index.isOdd ? oddItemColor : evenItemColor,
                  tileColor: oddItemColor,
                  title: Text('${titles[3]} $index'),
                );
              },
            ),
          ],
          
        ),
      ),
    );
  }
}