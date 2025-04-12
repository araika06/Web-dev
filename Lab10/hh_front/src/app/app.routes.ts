import { Routes, RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CompanyListComponent } from './components/company-list/company-list.component';
import { VacancyListComponent } from './components/vacancy-list/vacancy-list.component';

export const routes: Routes = [
    { path: '', redirectTo: 'companies', pathMatch: 'full' },
    { path: 'companies', component: CompanyListComponent},
    { path: 'vacancies', component: VacancyListComponent}
];

@NgModule ({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})

export class AppRoutingModule {}