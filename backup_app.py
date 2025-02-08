# backup_app.py (versão corrigida e melhorada)
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
import time
import threading
from datetime import datetime

class BackupApp:
    def __init__(self, root):
        self.root = root
        root.title("Backup Manager Pro")
        
        # Configuração de estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variáveis de controle
        self.paused = False
        self.cancelled = False
        
        # --- Menu Principal ---
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        
        # Menu Arquivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Nova Tarefa", command=self.add_backup_task)
        self.file_menu.add_command(label="Salvar Configurações", command=self.save_config)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=root.quit)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        
        # Menu Ajuda
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Sobre", command=self.show_about)
        self.menu_bar.add_cascade(label="Ajuda", menu=self.help_menu)

        # --- Barra de Ferramentas ---
        self.toolbar_frame = ttk.Frame(root)
        self.toolbar_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.buttons = [
            ('+ Tarefa', self.add_backup_task),
            ('- Tarefa', self.remove_backup_task),
            ('▶ Iniciar', self.start_backup),
            ('⏸ Pausar', self.pause_backup),
            ('⏹ Cancelar', self.cancel_backup)
        ]
        
        for text, cmd in self.buttons:
            btn = ttk.Button(self.toolbar_frame, text=text, command=cmd)
            btn.pack(side=tk.LEFT, padx=2)
        
        # --- Área de Tarefas ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.task_frames = []

        # --- Barra de Status ---
        self.status_bar = ttk.Label(root, text="Pronto", relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # ========== MÉTODOS PRINCIPAIS ==========
    def create_task_tab(self, task_name="Nova Tarefa"):
        task_frame = ttk.Frame(self.notebook)
        self.notebook.add(task_frame, text=task_name)
        
        # Variáveis da tarefa
        source_var = tk.StringVar()
        destination_var = tk.StringVar()
        
        # Widgets da tarefa
        ttk.Label(task_frame, text="Origem:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        ttk.Entry(task_frame, textvariable=source_var, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(task_frame, text="Procurar", 
                 command=lambda: self.select_folder(source_var)).grid(row=0, column=2, padx=5)
        
        ttk.Label(task_frame, text="Destino:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        ttk.Entry(task_frame, textvariable=destination_var, width=50).grid(row=1, column=1, padx=5)
        ttk.Button(task_frame, text="Procurar", 
                 command=lambda: self.select_folder(destination_var)).grid(row=1, column=2, padx=5)
        
        # Área de progresso
        progress = ttk.Progressbar(task_frame, orient=tk.HORIZONTAL, mode='determinate')
        progress.grid(row=2, column=0, columnspan=3, pady=10, sticky='ew')
        
        # Labels informativos
        status_label = ttk.Label(task_frame, text="Status: Aguardando início")
        status_label.grid(row=3, column=0, columnspan=3, sticky='w')
        
        task_data = {
            'frame': task_frame,
            'source_var': source_var,
            'destination_var': destination_var,
            'progress': progress,
            'status_label': status_label
        }
        
        self.task_frames.append(task_data)
        return task_data

    def select_folder(self, path_var):
        folder = filedialog.askdirectory()
        if folder:
            path_var.set(folder)
            self.update_status(f"Pasta selecionada: {folder}")

    # ========== CONTROLE DE BACKUP ==========
    def start_backup(self):
        self.cancelled = False
        self.paused = False
        for task in self.task_frames:
            if not self.validate_paths(task):
                continue
            threading.Thread(target=self.run_backup, args=(task,), daemon=True).start()

    def validate_paths(self, task):
        src = task['source_var'].get()
        dst = task['destination_var'].get()
        
        if not src or not dst:
            messagebox.showerror("Erro", "Defina origem e destino primeiro!")
            return False
            
        if not os.path.exists(src):
            messagebox.showerror("Erro", f"Pasta de origem não existe:\n{src}")
            return False
            
        return True

    def run_backup(self, task):
        src = task['source_var'].get()
        dst = task['destination_var'].get()
        
        try:
            total_files = sum(len(files) for _, _, files in os.walk(src))
            step = 100 / total_files if total_files > 0 else 0
            
            self.root.after(0, task['progress'].config, {'value': 0})
            self.root.after(0, task['status_label'].config, 
                          {'text': "Backup em andamento...", 'foreground': 'blue'})
            
            for root_dir, dirs, files in os.walk(src):
                if self.cancelled:
                    break
                
                while self.paused:
                    time.sleep(0.5)
                
                rel_path = os.path.relpath(root_dir, src)
                dest_dir = os.path.join(dst, rel_path)
                
                os.makedirs(dest_dir, exist_ok=True)
                
                for file in files:
                    if self.cancelled:
                        break
                    
                    src_file = os.path.join(root_dir, file)
                    dst_file = os.path.join(dest_dir, file)
                    
                    if os.path.exists(dst_file):
                        continue  # Pula arquivos existentes
                    
                    shutil.copy2(src_file, dst_file)
                    self.root.after(0, self.update_progress, task, step)
            
            if not self.cancelled:
                self.root.after(0, task['status_label'].config, 
                              {'text': "Backup concluído com sucesso!", 'foreground': 'green'})
                self.update_status("Operação concluída")
            else:
                self.root.after(0, task['status_label'].config, 
                              {'text': "Backup cancelado", 'foreground': 'orange'})
                
        except Exception as e:
            self.root.after(0, task['status_label'].config, 
                          {'text': f"Erro: {str(e)}", 'foreground': 'red'})
            self.root.after(0, messagebox.showerror, 
                          "Erro", f"Falha no backup:\n{str(e)}")

    def update_progress(self, task, step):
        task['progress']['value'] = min(task['progress']['value'] + step, 100)
        self.root.update_idletasks()

    def pause_backup(self):
        self.paused = not self.paused  # Corrigido operador lógico
        self.update_status("Backup pausado" if self.paused else "Backup retomado")
        self.pause_button.config(text="▶ Retomar" if self.paused else "⏸ Pausar")

    def cancel_backup(self):
        self.cancelled = True
        self.update_status("Backup cancelado pelo usuário")

    # ========== UTILITÁRIOS ==========
    def add_backup_task(self):
        new_task = self.create_task_tab()
        self.notebook.select(new_task['frame'])

    def remove_backup_task(self):
        if self.task_frames:
            current_tab = self.notebook.index("current")
            self.notebook.forget(current_tab)
            del self.task_frames[current_tab]

    def update_status(self, message):
        self.status_bar.config(text=message)
        self.root.update_idletasks()

    def save_config(self):
        messagebox.showinfo("Info", "Funcionalidade em desenvolvimento")

    def show_about(self):
        about_text = "Backup Manager Pro\nVersão 2.2\nDesenvolvido para Ubuntu"
        messagebox.showinfo("Sobre", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = BackupApp(root)
    root.mainloop()
