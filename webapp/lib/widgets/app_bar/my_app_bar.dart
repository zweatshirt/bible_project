import 'package:flutter/material.dart';


class MyAppBar extends StatelessWidget implements PreferredSizeWidget {

  final List<String> titles = <String>[
    'Book',
    'Chapter',
    'Verse Search',
    'Dictionary',
  ];
  
  MyAppBar({super.key});

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight + 18);

  @override
  Widget build(BuildContext context) {
  return AppBar(
      notificationPredicate: (ScrollNotification notification) {
        return notification.depth == 1;
      },
      // The elevation value of the app bar when scroll view has
      // scrolled underneath the app bar.
      scrolledUnderElevation: 4.0,
      shadowColor: Theme.of(context).shadowColor,
      bottom: TabBar(
        tabs: <Widget>[
          Tab(
            icon: const Icon(Icons.auto_stories),
            text: titles[0],
          ),
          Tab(
            icon: const Icon(Icons.article),
            text: titles[1],
          ),
          Tab(
            icon: const Icon(Icons.search_rounded),
            text: titles[2],
          ),
          Tab(
            icon: const Icon(Icons.read_more),
            text: titles[3],
          )
        ],
      ),
    );
  }
}