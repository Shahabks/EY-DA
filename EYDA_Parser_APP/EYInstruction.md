# Documents Parsing Script

This script parses documents into markdown format with cleaned text output using LlamaParse. It accepts an optional prompt instruction file and parses the given documents with noise removed.


このスクリプトは、LlamaParse を使用して PDF, xls, doc, ppt, html などのドキュメントをマークダウン形式に変換し、OCR のノイズを除去したテキスト出力を生成します。任意でプロンプト指示ファイル（例: prompt_inst.txt）を読み込み、ドキュメント解析時に活用することも可能です。

## 前提条件

- Python 3.x
- 以下の Python パッケージが必要です（pip を使ってインストールしてください）:

  ```bash
  python -m pip install nest_asyncio python-dotenv llama-cloud-services llama-index-core
  ```

## 使い方

このスクリプトは、ハードコードされたパスに依存しないようにコマンドライン引数を使用します。ユーザーは実行時に入力ファイル、（任意の）プロンプト指示ファイル、出力ファイルのパスを指定することができます。

### コマンドライン引数

- `--input`: **（必須）** 入力 PDF ファイルのパス。
- `--prompt`: **（任意）** カスタムプロンプト指示ファイル（例: `prompt_inst.txt`）のパス。指定しない場合、カスタム指示は無効になります。
- `--output`: **（任意）** 出力マークダウンファイルのパス。指定がない場合は、入力ファイルと同じディレクトリに入力ファイル名を基に `-parsed_output.md` として保存されます。

### 実行例

たとえば、Windows や他の OS で以下のように実行します:

```bash
python Parse.py --input "C:\path\to\your\document.pdf" --prompt "C:\path\to\prompt_inst.txt" --output "C:\path\to\output\your_output.md"
```

プロンプトファイルが不要な場合は、`--prompt` オプションを省略して実行してください:

```bash
python Parse.py --input "C:\path\to\your\document.pdf"
```

出力ファイルのパスが指定されていない場合、出力は入力ファイルと同じディレクトリに保存されます。

## 動作概要

1. **カスタム指示の読み込み**:  
   指定されたプロンプト指示ファイル（prompt_inst.txt）がある場合、その内容を読み込みます。ファイルが見つからない、または指定がない場合は、カスタム指示は無効になります。

2. **PDF の解析**:  
   LlamaParse パーサーを使用して、提供された API キーおよび追加オプションで PDF を解析します。解析は複数行の出力や、OCR ノイズの除去に対応しています。

3. **出力の保存**:  
   解析後のマークダウン形式の出力は、指定された出力ディレクトリまたは入力ファイルと同じディレクトリに保存されます。

## 環境変数

Llama Cloud の API キーは、環境変数または `.env` ファイル（[python-dotenv](https://pypi.org/project/python-dotenv/) パッケージ使用）で設定することができます。スクリプトはデフォルトで `LLAMA_CLOUD_API_KEY` 環境変数の値を使用し、見つからない場合はプレースホルダーキーを利用します。

## 注意事項

- 指定するファイルパスが有効であり、スクリプトがそれらのディレクトリに対して読み書き権限を持っていることを確認してください。
- このスクリプトはできるだけ汎用的に設計されています。ハードコードされたパスを変更する手間なく、他のユーザーと共有が可能です。
- Google Colab や他の OS で使用する場合、ファイルパスの形式やディレクトリのマウント方法（例: Google Drive のマウント）に合わせた調整を行ってください。

-------------------------------------------------------------------------------------

## Prerequisites

- Python 3.x
- The following Python packages (install via pip):

  ```bash
  python -m pip install nest_asyncio python-dotenv llama-cloud-services llama-index-core
  ```

## Usage

The script is designed to work in a universal way, allowing users to specify file paths via command-line arguments rather than hardcoded paths.

### Command-Line Arguments

- `--input`: **(Required)** Path to the input PDF file.
- `--prompt`: **(Optional)** Path to a custom prompt instruction text file (e.g., `prompt_inst.txt`). If not provided, the script will run without a custom prompt.
- `--output`: **(Optional)** Desired path for the output markdown file. If not provided, the output file is saved in the same directory as the input file, with the same base name appended by `-parsed_output.md`.

### Example Command

On Windows or any OS, run the script from the command line like this:

```bash
python Parse.py --input "C:\path\to\your\document.pdf" --prompt "C:\path\to\prompt_inst.txt" --output "C:\path\to\output\your_output.md"
```

If you do not have a prompt file, simply omit the `--prompt` option:

```bash
python Parse.py --input "C:\path\to\your\document.pdf"
```

The script will automatically save the output markdown file in the input file's directory if the `--output` option is not specified.

## How It Works

1. **Loading Custom Instructions**:  
   The script attempts to load a custom prompt instruction file if provided. If the file cannot be found or is not provided, the script will run without a custom prompt.

2. **Parsing the PDF**:  
   The script uses the LlamaParse parser with the provided API key and additional options that handle multiline, structured outputs and noise removal.

3. **Saving the Output**:  
   The parsed markdown output is saved into a file in the specified output directory or in the same folder as the input file.

## Environment Variables

The API key for Llama Cloud can be set either in your environment or within a `.env` file (using the [python-dotenv](https://pypi.org/project/python-dotenv/) package). The script uses the environment variable `LLAMA_CLOUD_API_KEY` by default, falling back to a placeholder key if not found.

## Notes

- Ensure that the file paths you provide are valid and that the script has read/write permissions for those directories.
- This script is designed to be universal. You can share it with others without needing to update hardcoded paths.
- If using in environments like Google Colab or a different OS, ensure corresponding adjustments for file path formats and mounting of directories (e.g., using Google Drive in Colab).

