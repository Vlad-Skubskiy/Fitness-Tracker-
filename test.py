import sys
import mediapipe as mp

print(f"🐍 Версия Python: {sys.version}")
print(f"📦 Версия MediaPipe: {getattr(mp, '__version__', 'Не определена')}")
print(f"📁 Путь к MediaPipe: {getattr(mp, '__file__', 'Не найден')}")
print(f"🔍 Что есть внутри mp: {dir(mp)}")