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
export function deactivate() {
    vscode.window.showInformationMessage('Range Engine extension deactivated.');

    const stubsPath = vscode.workspace.getConfiguration('python').get<string[]>('analysis.extraPaths') || [];

    // Remove path from stubs if it is set
    const updatedPaths = stubsPath.filter((path) => !path.includes('src/stubs'));
    vscode.workspace.getConfiguration('python').update(
        'analysis.extraPaths',
        updatedPaths,
        vscode.ConfigurationTarget.Workspace
    );
}
