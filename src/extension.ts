// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as path from 'path';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
	// Event to monitor when a document is opened
    vscode.workspace.onDidOpenTextDocument((document) => {
        handleDocument(document, context);
    });

    // Event to monitor edits to the document
    //vscode.workspace.onDidChangeTextDocument((event) => {
    //    handleDocument(event.document, context);
    //});

    // For files already opened when activating the extension
    vscode.workspace.textDocuments.forEach((document) => {
        handleDocument(document, context);
    });

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	/*const disposable = vscode.commands.registerCommand('range-engine-api.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from Range Engine API!');
	});

	context.subscriptions.push(disposable);*/
}

async function handleDocument(document: vscode.TextDocument, context: vscode.ExtensionContext) {
    if (document.languageId === 'python' &&
        (document.getText().includes('import Range') || document.getText().includes('from Range import'))) {
        const stubsPath = path.join(context.extensionPath, 'src/stubs');
        const config = vscode.workspace.getConfiguration('python');
        const extraPaths = config.get<string[]>('analysis.extraPaths') || [];

        // Only add the path if it is not already configured
        if (!extraPaths.includes(stubsPath)) {
            await config.update(
                'analysis.extraPaths',
                [...extraPaths, stubsPath],
                vscode.ConfigurationTarget.Workspace
            );
            //vscode.window.showInformationMessage('Range Engine detected! Autocomplete enabled.');
        }
    }
}

// This method is called when your extension is deactivated
export async function deactivate() {
    //console.log('Range Engine extension deactivated.');

    const config = vscode.workspace.getConfiguration('python');
    const extraPaths = config.get<string[]>('analysis.extraPaths') || [];
    const stubsPath = path.join(__dirname, 'src/stubs');

    // Remove path from stubs if it is set
    if (extraPaths.includes(stubsPath)) {
        const updatedPaths = extraPaths.filter((path) => path !== stubsPath);
        await config.update('analysis.extraPaths', updatedPaths, vscode.ConfigurationTarget.Workspace);
        vscode.window.showInformationMessage('Range Engine autocomplete disabled.');
    }
}
