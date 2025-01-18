import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:image2text/blocs/bloc/picker_image_bloc.dart';
import 'package:image2text/views/home_view.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(const Image2Text());
}

class Image2Text extends StatelessWidget {
  const Image2Text({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: BlocProvider(
        create: (context) => PickerImageBloc(),
        child: const HomeView(),
      ),
    );
  }
}
