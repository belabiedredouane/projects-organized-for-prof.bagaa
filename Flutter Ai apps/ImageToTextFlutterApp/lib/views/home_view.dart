import 'package:flutter/material.dart';
import 'package:image2text/widgets/home_view_body.dart';

class HomeView extends StatelessWidget {
  const HomeView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 10,
        shadowColor: const Color(0xff3A2F2F),
        backgroundColor: const Color(0xff3A2F2F),
        title: const Text(
          'Text Recognision',
          style: TextStyle(
            fontFamily: 'ProtestRevolution-Regular',
            color: Colors.white,
          ),
        ),
      ),
      body: const HomeViewBody(),
    );
  }
}
